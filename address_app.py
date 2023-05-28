import config as config
from fastapi import FastAPI, HTTPException
from services.address_service import Address, AddressService
from plugins.google_plugins import geocode_address
from tools.geo_convert import gcj2bd

app = FastAPI()

@app.get("/address/resolver")
def address_resolver(
    raw_address: str | None = None
) -> Address:
    # use llm to resolve address
    address_service = AddressService(raw_address = raw_address)
    address = address_service.resolveAddress()
    # use google api to get latitude and longitude
    latitude = geocode_address(address.full_address)[0]
    longitude = geocode_address(address.full_address)[1]
    # convert google geo code to baidu geo code
    address.latitude = gcj2bd(latitude, longitude)[0]
    address.longitude = gcj2bd(latitude, longitude)[1]

    return address