# Create a Python dictionary of Cisco device IDs and model names

If you need to turn this https://communities.cisco.com/docs/DOC-46061 into a repeatable Python dictionary, this is the script for you!

admin:run sql select enum, name from typemodel
enum  name                                              
===== ================================================= 
15    EMCC Base Phone                                   
20    SCCP Phone                                        
30    Analog Access                                     
40    Digital Access                                    
42    Digital Access+                                   
43    Digital Access WS-X6608                           
47    Analog Access WS-X6624                            
50    Conference Bridge                                 
51    Conference Bridge WS-X6608                        
61    H.323 Phone                                       
62    H.323 Gateway                                     
70    Music On Hold                                     
71    Device Pilot                                      
72    CTI Port                                          
73    CTI Route Point                                   
80    Voice Mail Port                                   
90    Route List                                        
100   Load Simulator                                    
110   Media Termination Point                           
111   Media Termination Point Hardware                  
120   MGCP Station                                      
121   MGCP Trunk                                        
122   GateKeeper                                        
125   Trunk                                             
126   Tone Announcement Player                          
254   Unknown MGCP Gateway                              
255   Unknown                                           
52    Cisco IOS Conference Bridge (HDV2)                
53    Cisco Conference Bridge (WS-SVC-CMM)              
83    Cisco IOS Software Media Termination Point (HDV2) 
84    Cisco Media Server (WS-SVC-CMM-MS)                
112   Cisco IOS Media Termination Point (HDV2)          
113   Cisco Media Termination Point (WS-SVC-CMM)        
131   SIP Trunk                                         
132   SIP Gateway                                       
133   WSM Trunk                                         
134   Remote Destination Profile                        
85    Cisco Video Conference Bridge (IPVC-35xx)         
522   BlackBerry MVS Client with Voice over Wi-Fi       
30027 Analog Phone                                      
30028 ISDN BRI Phone                                    
2     Cisco 12 SP+                                      
3     Cisco 12 SP                                       
4     Cisco 12 S                                        
1     Cisco 30 SP+                                      
5     Cisco 30 VIP                                      
9     Cisco 7935                                        
6     Cisco 7910                                        
7     Cisco 7960                                        
8     Cisco 7940                                        
10    Cisco VGC Phone                                   
11    Cisco VGC Virtual Phone                           
48    VGC Gateway                                       
12    Cisco ATA 186                                     
124   7914 14-Button Line Expansion Module              
336   Third-party SIP Device (Basic)                    
374   Third-party SIP Device (Advanced)                 
115   Cisco 7941                                        
119   Cisco 7971                                        
20000 Cisco 7905                                        
302   Cisco 7985                                        
307   Cisco 7911                                        
308   Cisco 7961G-GE                                    
309   Cisco 7941G-GE                                    
335   Motorola CN622                                    
348   Cisco 7931                                        
358   Cisco Unified Personal Communicator               
365   Cisco 7921                                        
369   Cisco 7906                                        
375   Cisco TelePresence                                
30002 Cisco 7920                                        
30006 Cisco 7970                                        
30007 Cisco 7912                                        
30008 Cisco 7902                                        
30016 Cisco IP Communicator                             
30018 Cisco 7961                                        
30019 Cisco 7936                                        
30032 SCCP gateway virtual phone                        
30035 IP-STE                                            
404   Cisco 7962                                        
412   Cisco 3951                                        
431   Cisco 7937                                        
434   Cisco 7942                                        
435   Cisco 7945                                        
436   Cisco 7965                                        
437   Cisco 7975                                        
446   Cisco 3911                                        
497   Cisco 6961                                        
564   Cisco 6945                                        
478   Cisco TelePresence 1000                           
582   Generic Single Screen Room System                 
480   Cisco TelePresence 3200                           
227   7915 12-Button Line Expansion Module              
232   CKEM 36-Button Line Expansion Module              
479   Cisco TelePresence 3000                           
495   Cisco 6921                                        
548   Cisco 6911                                        
550   Cisco ATA 187                                     
481   Cisco TelePresence 500-37                         
591   Cisco TelePresence 1300-47                        
468   Cisco Unified Mobile Communicator                 
503   Cisco Unified Client Services Framework           
580   Cisco E20                                         
496   Cisco 6941                                        
562   Cisco Dual Mode for iPhone                        
577   Cisco 7926                                        
558   Cisco TelePresence 400                            
493   Cisco 9971                                        
557   Cisco TelePresence 200                            
588   Generic Desktop Video Endpoint                    
520   Cisco TelePresence 1100                           
547   Cisco 6901                                        
583   Generic Multiple Screen Room System               
228   7915 24-Button Line Expansion Module              
230   7916 24-Button Line Expansion Module              
540   Cisco 8961                                        
537   Cisco 9951                                        
229   7916 12-Button Line Expansion Module              
505   Cisco TelePresence 1300-65                        
590   Cisco TelePresence 500-32                         
484   Cisco 7925                                        
521   Transnova S3                                      
593   Cisco Cius                                        
618   VzWMUC                                            
527   IPTrade TAD                                       
541   Telecore 2151                                     
638   Intelbras TIP100                                  
523   BlackBerry MVS Client                             
639   Avara SIP30                                       
575   Cisco Dual Mode for Android                       
651   Intelbras ATA GKM2210T                            
451   IPTrade Profile EK            
