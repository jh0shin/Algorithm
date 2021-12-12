# Computer network

#### Protocol
- Define format, order of messages sent and received
#### Layering
- Dealing with complex systems
- Modularization eases maintenance, updating of system
1. Application : supporting network applications - FTP, SMTP, HTTP
2. Transport : process-process data transfer - TCP, UDP
3. Network : routing of datagrams from source to dest - IP, routing protocols
4. Link : data transfer between neighboring network elements - Ethernet, 802.111
5. Physical : bits ***on the wire***
#### ISO reference model
- Application / Presentation / Session / Transport / Network / Link / Physical
1. Presentation : allow applications to interpret meaning of data - encryption, compression
2. Session : synchronization, checkpointing, recovery of data exchange

## Application Layer
- Client-server
- P2P
#### Socket
- process sends/receives messages to/from its **socket**
#### Internet transport protocol service
- TCP service
    - reliable transport
    - flow control, congestion control
    - does not provice : timing, minimum throughput guarantee, security
- UDP service
    - unreliable data transfer
    - does not provice : reliability, flow control, congestion control,
      timing, minimum throughput guarantee, security
    - But faster than TCP
    - Streaming or internet telephony
#### HTTP
- HyperText Transfer Protocol
- Web's application layer protocol
- Use TCP (port 80)
- non-persistent HTTP
    - at most one object over TCP connection (then closed)
    - downloading multiple objects required multiple connections
    - open connection(C) -> accept(S) -> request message(C) -> response, close(S)
      -> receive(C)
    - RTT : time for small packet to travle from client to server and back
    - response time : 2RTT + file transmission time (packet L / link bandwidth * n)
- persistent HTTP
    - multiple objects can be sent over single TCP connection
#### Cookie
1. Cookie header line of HTTP response message
2. Cookie header line in next HTTP request message
3. Cookie file kept on user's host, manages by user's browser
4. back-end database at web site
- What cookies can be used for : authorization, recommendation, user session state
- Aside : privacy
#### Web caches (proxy server)
- Goal : satisfy client request without involving origin server
- Reduce response time for client request
- Reduce traffic on an institution's access link
#### SMTP (Electronic mail)
- Uses TCP to reliably transfer email message from client to server, port 25
#### DNS (Domain Name System)
- Distributed database implemented in hierarchy of many name servers
- Application-layer protocol : communicate to resolve names
- DNS services : hostname to IP address translation, host aliasing, load distribution
- Why not centralize? : single point of failure, traffic volume, distant, maintenance
- Root name servers : contacted by local name server that can not resolve name
- TLD(Top-Level Domain) servers : responsible for com, org, net, edu and country domain
- Authoritative DNS servers : organization's own DNS servers
- Local DNS name server : each ISP has one
- DNS name resolution : iterated query / recursive query
#### P2P architecture
- no always-on server
- arbitrary end systems directly communicate
- peers are intermittently connected and change IP address
#### CDN (Content Distribution Network)
- Video traffic : major consumer of internet bandwidth
- Solution : distributed, application-level infrastructure
- Store/serve multiple copies of videos at multiple geographically distribued sites
- DASH : Dynamic, Adaptive Streaming over HTTP
- OTT : Netflix ...

## Transport layer
#### Transport services and protocols
- Provide logical communication between app processes running on different hosts