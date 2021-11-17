x-terminal-emulator -e python3 central.py
sleep 2
x-terminal-emulator -e python3 front.py
sleep 2
export BLINKA_MCP2221=1
python3 sensor.py
