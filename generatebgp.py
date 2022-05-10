def bgp_config_ios_global(asn , rid):

    bgp_config_ios_global =    [
                       'router bgp %s' % asn ,
                       'bgp router-id %s' % rid                   
                       ]
    return bgp_config_ios_global

def bgp_config_ios_neigh(asn , neigh_ip):

    bgp_config_ios_neigh =    [                   
                       'neighbor %s remote-as %s' % (neigh_ip , asn) ,
                       'neighbor %s update-source loopback 0' % neigh_ip ,
                       'neighbor %s next-hop-self' % neigh_ip
                       ]
    return bgp_config_ios_neigh

###############   bgp config   nexus base generator functions    ######################


def bgp_config_nx_global(asn , rid):

    bgp_config_nx_global =   [ 
                       'router bgp %s' % asn , 
                       'router-id %s' % rid                   
                       ]

    return bgp_config_nx_global

def bgp_config_nx_neigh(asn , neigh_ip):

    bgp_config_nx_neigh =    [                 
                       'neighbor %s remote-as %s' %(neigh_ip , asn) ,
                       'update-source loopback 0' ,
                       'address-family ipv4 unicast' ,
                       'next-hop-self'
                       ]

    return bgp_config_nx_neigh

#############################

def iosxe(asn, myloopback, otherloopbacks):
  bgpios = []
  bgpios += bgp_config_ios_global(asn, myloopback)
  for neigh in otherloopbacks:
    if neigh != myloopback:
        bgpios += bgp_config_ios_neigh(asn, neigh)
  return bgpios

##################################################



def nxos(asn, myloopback, otherloopbacks):
  bgpnx = []
  bgpnx += bgp_config_nx_global(asn, myloopback)
  for neigh in otherloopbacks:
    if neigh != myloopback:
        bgpnx += bgp_config_nx_neigh(asn, neigh)
  return bgpnx

if __name__ == "__main__":

  cfgios = iosxe('65000' , '1.1.1.1' , ['1.1.1.1','2.2.2.2' , '3.3.3.3'])

  print(cfgios)

  cfgnxos = nxos('65000' , '1.1.1.1' , ['1.1.1.1', '2.2.2.2' , '3.3.3.3'])

  print(cfgnxos)
