## About

PytR is a  Tracker written in Python using non-blocking Tornado Web Server. It also features a nice and clean UI for showing Tracker statistics.

__Work In Progress__: _May not work as a fully functioning Torrent Tracker_.

## Installing virtualenv 
    [sudo] pip install virtualenv

## Setting up a virtual environment
    virtualenv virtual
    
## Activate the virtual environment
    source virtual/bin/activate


## Installing Tornado
    
    [sudo] pip install tornado


## Installing Pytr

To install Pytr, run

	sudo python setup.py install

## Configuring Pytr

Edit `~/.pytr/config/pytr.conf` and change the values to your choice. The following options are available.

- `port`: Pytt will listen to this port
- `interval`: Interval in seconds that the client should wait between sending regular requests to the tracker.
- `min_interval`: Minimum announce interval. If present clients must not re-announce more frequently than this.

## Running Pytr

To run Pytr, do

	python tracker.py -b

or

	pytr -d

- `-p` or `--port` (optional): To specify port
- `-d` or `--debug` (optional): Enable debug mode
- `-b` or `--background` (optional): Run as a daemon process

## License

MIT License. Refer COPYING for more info.

## Note

if you are inside a virtualenviroment, the sudo command is not necessary.
