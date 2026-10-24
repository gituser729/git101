"""Estimate whether a fictional landing-page test meets its signup target."""

landing_page_visitors = 200
email_signups = 18
target_conversion_rate = 10

conversion_rate = email_signups / landing_page_visitors * 100

print("Landing-page visitors:", landing_page_visitors)
print("Email signups:", email_signups)
print("Signup conversion rate:", round(conversion_rate, 1), "%")
print("Target conversion rate:", target_conversion_rate, "%")

if conversion_rate >= target_conversion_rate:
    print("The test met its target. Consider planning a larger pilot.")
else:
    print("The test is below its target. Consider revising the offer or testing again.")
