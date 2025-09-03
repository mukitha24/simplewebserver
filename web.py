from http.server import HTTPServer, BaseHTTPRequestHandler

content = '''
<!DOCTYPE html>
<html>
<head> <title> data</title>
</head>
<body> 
    <table align="center" border ="1" cellpadding="10" style="background-color: black; color: white;">
        <caption>List of protocols in tcp/ip protocols</caption>
        <tr><th>S.No</th><th>Name of the layer</th><th>Name of the protocols</th></tr>
        <tr><td>1 </td><td>Application layer</td><td>HTTP,FTP,DNS,Telnet</td></tr>
        
        <tr><td>2 </td><td>Transport layer</td><td>TCP/UDP</td></tr>
        <tr><td>3 </td><td>Network layer</td><td>IPV4/IPV6</td></tr>
        <tr><td>4 </td><td>Linl layer</td> <td>Ethernet</td></tr>


    </table>
</body>'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()