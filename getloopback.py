from ncclient import manager as MG

ns = {'ios':'http://cisco.com/ns/yang/Cisco-IOS-XE-native' , 'nx' : 'http://cisco.com/ns/yang/cisco-nx-os-device'}

xpath_ios = './ios:native/ios:interface/ios:Loopback/ios:ip/ios:address/ios:primary/ios:address'
xpath_nx = './nx:System/nx:ipv4-items/nx:inst-items/nx:dom-items/nx:Dom-list/nx:if-items/nx:If-list/nx:addr-items/nx:Addr-list/nx:addr'



def nxos(mgmtip, user, pw):

    with MG.connect(host = mgmtip,
                    port = 830,
                    username = user,
                    password = pw,
                    hostkey_verify = False,
                    device_params = {'name' : 'nexus'},
                    allow_agent = False,
                    look_for_keys = False
                            ) as session:
        filter_nx = '''
        <System xmlns="http://cisco.com/ns/yang/cisco-nx-os-device">
    <ipv4-items>
      <inst-items>
        <dom-items>
          <Dom-list>
          <name>default</name>
            <if-items>
              <If-list>
              <id>lo0</id>
                <addr-items>
                  <Addr-list>
                    <addr/>
                  </Addr-list>
                </addr-items>
              </If-list>
            </if-items>
          </Dom-list>
        </dom-items>
      </inst-items>
    </ipv4-items>
  </System>


                '''


        repl = session.get_config('running', filter = ('subtree', filter_nx))

        

    #print(repl)
    root = repl.data_ele
    loop_addr_obj = root.findall(xpath_nx , ns)
    loop_addr = loop_addr_obj[0].text[:-3]
    print(loop_addr)
    return loop_addr
    
def iosxe(mgmtip, user, pw):

    with MG.connect(host = mgmtip,
                    port = 830,
                    username = user,
                    password = pw,
                    hostkey_verify = False,
                    device_params = {'name' : 'iosxe'},
                    allow_agent = False,
                    look_for_keys = False
                            ) as session:
        filter_iosxe = '''
        <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <interface>
      <Loopback>
      <name>0</name>
        <ip>
          <address>
            <primary>
              <address/>
              <mask/>
            </primary>
          </address>
        </ip>
      </Loopback>
    </interface>
  </native>


                '''


        repl = session.get_config('running', filter = ('subtree', filter_iosxe))

        

    #print(repl)
    root = repl.data_ele
    loop_addr_obj = root.findall(xpath_ios , ns)
    loop_addr = loop_addr_obj[0].text
    print(loop_addr)
    return loop_addr
    
if __name__ == "__main__":
    nxos('10.0.0.100', 'student', 'L1nux_dc')
    iosxe('10.0.0.101', 'student' , 'L1nux_dc')
    iosxe('10.0.0.102', 'student' , 'L1nux_dc')
