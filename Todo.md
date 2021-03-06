# To Do:
- Display server database in simple webpage for debugging?
- Update client connection system to just have server constantly (every 60s) broadcast json with ip address?
- Reject connection based on name or IP, decide accordingly?
- Protect data upload based on name not IP, or both name and IP?
- Add mechanism for arbitrary connection to poll the total database state? (debugging only)
- Add handling for duplicate clients wanting to update same field with potentially different values?
  - Maybe a mapping of {IP: value} with something to filter to most relevant value?
    - Sounds too complicated. Maybe just read field before updating in each of the implementations
- Client group option within client and captive portal
  - Serves as intermediate step to adding a grouping webpage
- Add server webpage to create groupings for clients
  - eg "Living Room Lights" = ["Light1", "Light2", "Light3"]
  - This would allow for voice commands to allow for individual lights to be switched or all at once
- Add mechanism for registered fields to specify how protected the write access is
- Refactor voice command regexes to include a callback
  - This would potentially simplify regex loops
- Factor out sound player so that other functions can use it
  - eg. timer alarms
- Add other functions to voice assistant
  - [Done] Simple listening sounds
  - [Done] Snowboy on raspberry pi
  - [Partially Done] Timers
  - Alarms
  - Spotify via pyspotify & libspotify
  
## Client ideas:
- [Done] Voice control client
- Email client for field
  - Send email when field value changes

## Done:
- Server to store timestamp of last data submission
- Clients declare to server name
- Server to approve client name or suggest alternative
- Update all client/server interactions to use json
- Server to serve requested data in json format
- Clients declare to server data types to be reported
- Server to add client data types to database
- Server to allow submission of data from registered IP addresses
- Return timestamp with polled data
- Make client generic so that there is an abstract method which contains the specific implementation
- Work out how to serve multiple clients simultaneously
- Update client server poller to not use threads so that it can work on esp8266 modules
- Make Epoch time polling client example
- Make micropython compliant client
- ESP8266 button pressed client
- ESP8266 connection code with hard-coded authentication details factored out into json file
- Add script to move files to correct places on ESP8266
- Allow request for all data types available
- Handle missing data when polling
- Add mechanism for ESP8266 to be come an access point with a login page when no wifi credentials found
- Handle clients and server disconnecting and reconnecting
- Lock database when client request comes in
- Store names in Interface client thread so that removal of a client removes the actual client, not just the first client with the given IP address
- Store the device name in a .json file so that devices don't change names after a power cut
- Add handling for readding the fields when the server disconnects from the client
- Add device name as option on esp8266 login
- Allow requesting of multiple data types in a single request