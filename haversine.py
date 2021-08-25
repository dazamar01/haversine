from haversine_lib import Haversine  

longitud_origen = -103.43450819781592
latitud_origen = 20.68133628771169

longitud_destino = -103.43520910921957
latitud_destino = 20.67817182165015

print(Haversine([longitud_origen,latitud_origen],[longitud_destino,latitud_destino]).meters )

# https://nathanrooy.github.io/posts/2016-09-07/haversine-with-python/

# ##############
# CASA 20.679747480050104, -103.43515807398528

# longitud_origen = -103.4351439551733
# latitud_origen = 20.679730190021385

# longitud_destino = -103.43397562688546
# latitud_destino = 20.679498074618124