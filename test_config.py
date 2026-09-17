from config import get_config

current_config = get_config()

print(f"Debug Modu: {current_config.DEBUG}")
print(f"Veritabanı URL: {current_config.DATABASE_URL}")
print(f"AI Provider: {current_config.AI_PROVIDER}")
print(f"Business Context: {current_config.BUSINESS_CONTEXT}")
