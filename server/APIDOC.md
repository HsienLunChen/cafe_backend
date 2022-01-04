
## Request Cafe based on city and district
**Request Format:** /cafe/city

**Request Type:** GET

**Returned Data Format**: JSON

**Description:** Return a list of cafe object

**Required query parameter:** city, order, weekday

**Example Request:** /cafe/city with GET parameters of `city=台北市`, `district=松山區`, `weekday=Mon`, `order=rating`, `detail=true`, `now=1600`, `quiet=1`, `socket=yes`

**Example Response:**
``` json
[
    {
        "cafeid": 576,
        "mrt": "內湖",
        "name": "此刻cafe&brunch",
        "address": "114台北市內湖區康寧路一段139號",
        "wifi": 1,
        "quiet": 4,
        "limited_time": "no",
        "socket": "yes",
        "googleMapLink": "https://maps.google.com/?cid=10109975412046711457",
        "lat": 25.0493662,
        "lng": 121.5544249,
        "city": "台北市",
        "district": "松山區",
        "phoneNumber": "02 2578 8129",
        "rating": 4.7,
        "numRatings": 114,
        "priceLevel": 2,
        "photo1": "Aap_uEC3fq2fgaqvtsVl2s_IJsFH0Ju6TL3OUOivnFZcAokF5rrXZREBo1t9sg3CnOSZCC36K_0ZTnA65fQEqVNRbBtguw5Y7tfi69R_3oIhjkn24oiUkfVrRjEhxXlxbtL05pMW-eiHHzP_NRFMNZ5lhNHD263nKxs3zbTUFeZ2dZvwkHDl",
        "photo2": "Aap_uECBKoCN9gGSX_UMsBPSL4Q8IOy7bEOyhCsZTFpq6bd83dTVEcub-vDGDXs9Fcr_75VFYVYeJiDRm9FRtXk6v10JD-RUufhgZUr4fdAwLYphm5kIdRtIWFF3qfyh89G--2ej-xxIlmkadhCV0qp-bXhJzH7nDV-hk6bGXXD8q8K7Cnbp",
        "photo3": "Aap_uEDpXy-bQr4VY4-087uERdI_ab47hMJ7Gtxl7KGTTQacfSv8utpktyMqJKbcFcDMp_BcYv4q_Evm42YsTLzQt4mPjIEoVwKZfilJ8ql2KH3LFHdX0KmDLWapPkPrN-k3p-9P2P22FdLKEs9qrhnTT6aRIrUodvcDCe0YsvymhpCCMSsG",
        "photo4": "Aap_uEBAVegU78zPq0QffmDOVZ7oWya9IRYxAsCxJRQY0EUGawet_pJwvKZdcK4b2gWqxmMpkgnpKIM9i030Mknoq6c12OYUXLfgdJE2XPUBgq6dfA_73QWX-NPFQq7WkA-fHLOUVODDg12vLlj7_L6LeESsdglFEr08kQyKyuXnbi-azNHn",
        "photo5": "Aap_uEDNfskPBS53J3TD1HLH-1Kqfq-pRi7M4UD8Y5XiUvJSDTkITclqZwmmUn0p3ZpyINvGRtDFrG1WkI4aCjSzgLZsAE04VZ4BK8Kys_eGuZTWKBETeeEDrbu9EU0yryvMrcXep90GNVUN7kdidARpWo7yKpGv89KtxWvanli1iKGB6LT-",
        "SunOpen": 1130,
        "SunClose": 2000,
        "MonOpen": 700,
        "MonClose": 1700,
        "TueOpen": 700,
        "TueClose": 1700,
        "WenOpen": 1130,
        "WenClose": 1900,
        "ThuOpen": 1130,
        "ThuClose": 1900,
        "FriOpen": 1130,
        "FriClose": 1900,
        "SatOpen": 1130,
        "SatClose": 2000
    },
    {
        "cafeid": 662,
        "mrt": "南京復興",
        "name": "ABOUT COFFEE",
        "address": "105台北市松山區南京東路三段256巷28弄19號1樓",
        "wifi": 1,
        "quiet": 4,
        "limited_time": "no",
        "socket": "yes",
        "googleMapLink": "https://maps.google.com/?cid=414018030731328765",
        "lat": 25.049874,
        "lng": 121.545247,
        "city": "台北市",
        "district": "松山區",
        "phoneNumber": "02 2731 8266",
        "rating": 4.7,
        "numRatings": 114,
        "priceLevel": 1,
        "photo1": "Aap_uECSNyumCoUS6x_s6qXNkEoxRayC4iZ_WZVOETfWI8hJg46kqJKax39-gn3bII_XskO_ohPi_CAEtDT2TxUJ-mTEz8VO2FaSxbnOTCPctxzismYhnqKZiLKYsIAFRaoTXmVjyVTzw_pnykXerel-y9R6xmQcKNlMAJxOrf835XsAivhH",
        "photo2": "Aap_uEDv9g8O_OhoqAnvn78LZ9LOF-X9Cgabrypf6FlbabLKtHUUeButWAiyvaV_RSaDyshxFeZonOfFCk55qbn_lMHpahiexYTO74m2YuwhnMgike-5GXG9lV3InGclxjaL-6PexoTJ4_yEUoQl0M_8Gk-95zvaBUbMAtkJzCsGC1xL0crL",
        "photo3": "Aap_uEDRHuSdiNRwK1TNw5uxdfjpGvUY11DEmtGY0r4PwyVBVz4rj970Y-c61NPf1k4hV_6RbSUzZ_jqslT6sNdYlqasoX26puPGRdSFdtqYOjeRZKTjpKno7l0BuL3dXEsCH2ilwbjmZ6aGA7qe6MA9Tx9AW9D9PsCGm7w_eGmiuw8UvV8a",
        "photo4": "Aap_uEBRvLa5U5MRTlYKQnxhp7fI_sqpQE60wsy5C9HlSWtE9g6zKzHvoT9HDAxhd94Qt05bxOHatuVNA74cr8U4OqHY6dqiMf__C8FmnG2hm1o9L6y37FREJlEmIrohATG1KouQd2fFauQBYNbO5brTPjdrfqay5-Lmgzrj2Lm1X5eJ2tNy",
        "photo5": "Aap_uECsiG9fkrB7Y4Y_ErRg6Evi6qjpsFT4nofkVFXxaenEnYyIYoS8juPa0Iz5kF6LtY1yTq5mtAMNNSrIou4cJwQyTjcuqTje6l8f40cij655AvRFKtCk4cRB_5Zezgm-wZEM1viRrdRRaA3N81hFbnPUeQZohjJ9C3ZEnWPJfNxjxtZv",
        "SunOpen": "",
        "SunClose": "",
        "MonOpen": 800,
        "MonClose": 1630,
        "TueOpen": 800,
        "TueClose": 1630,
        "WenOpen": 800,
        "WenClose": 1630,
        "ThuOpen": 800,
        "ThuClose": 1630,
        "FriOpen": 800,
        "FriClose": 1630,
        "SatOpen": "",
        "SatClose": ""
    }
]
```



## Request Cafe based on mrt
**Request Format:** /cafe/mrt

**Request Type:** GET

**Returned Data Format**: JSON

**Description:** Return a list of cafe object

**Required query parameter:** mrt, order, weekday

**Example Request:** /cafe/city with GET parameters of `weekday=Mon`, `order=rating`, `mrt=臺北車站`, `quiet=true`, `detail=true`

## Request Cafe based on just criteria
**Request Format:** /cafe

**Request Type:** GET

**Returned Data Format**: JSON

**Description:** Return a list of cafe object

**Required query parameter:**  order, weekday, quiet

**Example Request:** /cafe/city with GET parameters of `weekday=Mon`, `order=rating`, `quiet=true`, `detail=true`


## Query Parameters

For detail search in MRT and City query, set `detail=true`

order: rating, priceLevel

weekday: Mon, Tue, Wen, Thu, Fri, Sat, Sun

now: 1600

socket, wifi, limited_Time: set to true if the criteria is selected

quiet: 1, 2, 3

1. 安靜
2. 適中
3. 熱鬧

