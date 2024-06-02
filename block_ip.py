import subprocess
from cortexutils.responder import Responder

class BlockIP(Responder):
    def __init__(self):
        Responder.__init__(self)

    def run(self):
        ip = self.get_param('data.data', None, "IP address is missing")

        if not ip:
            self.error("No IP address provided to block")

        try:
            # Command to block the IP using ufw
            result = subprocess.run(['sudo', 'ufw', 'deny', 'from', ip], capture_output=True, text=True)

            if result.returncode == 0:
                self.report({'message': f'Successfully blocked IP: {ip}'})
            else:
                self.error(f"Failed to block IP: {ip}. Error: {result.stderr}")

        except Exception as e:
            self.error(f"Exception occurred: {str(e)}")

if __name__ == '__main__':
    BlockIP().run()
