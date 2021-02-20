#%%
import OctopusEnergyAPIWrapper.api as api
import pprint
pp = pprint.PrettyPrinter(indent=2)
client = api.api("test")
pp.pprint(client._get("/products/")['results'])
a=client._get("/products/")
pprint(type(a))
#print(json.dumps(json.loads(a.text), indent=4, sort_keys=True))