from google import genai

api_key = "AQ.Ab8RN6JvavraQhLUIBB8USDTwDNxVCny8LCfg5ZZTXi_sa1UNA"

client = genai.Client(api_key=api_key)

prompt="what is ai agent in simple words"

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

print(response.txt)