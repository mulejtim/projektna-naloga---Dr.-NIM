import bottle
from model import dr_nim
igra = dr_nim()

@bottle.get('/')
def racunalnik():
    return bottle.template('navodila.tpl.')

@bottle.get('/igralec/')
def igralec():
    po_izbiri = len(igra.zogice)
    igra.racunalnik()
    st_zogic = len(igra.zogice)
    if po_izbiri - 1 == st_zogic:
        ostale_zogice = 'racunalnik je izbral 1 zogico'
    else:
        ostale_zogice = 'racunalnik je izbral 2 zogice'
    if po_izbiri > 2:
        return bottle.template('igralec.tpl', st_zogic = st_zogic,
         ostale_zogice = ostale_zogice)
    elif 0 < po_izbiri <= 2:
        return bottle.template('izgubil.tpl', ostale_zogice = ostale_zogice)
    else:
        return bottle.template('zmagal.tpl')

@bottle.post('/igralec_prvic/')
def igralec():
    n = int(bottle.request.forms['n'])
    igra.dodaj(n) 
    if len(igra.zogice) > 2:
        return bottle.template('igralec.tpl',st_zogic = n,
         ostale_zogice = 'ti prvi izberi' )
    else:
        return bottle.template('bojecka.tpl')


@bottle.get('/vzemi/<stevilo>/')
def vzami(stevilo):
    igra.odstej(stevilo)
    bottle.redirect('/igralec/')



bottle.run(debug=True, reloader=True)