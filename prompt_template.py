data_masking_prompt = """

You are tasked with masking personally identifiable information (PII) in insurance claim documents. Your goal is to 
protect the privacy of individuals while maintaining the overall structure and readability of the document.

Here is the insurance claim document you need to process:

<document>
    {INSURANCE_CLAIM_DOCUMENT}
</document>

Follow these steps to mask the PII data:

1. Identify the following types of PII data in the document:
   - Patient names (first name, last name, or full name)
   - Dates of birth
   - Insurance ID numbers
   - Social Security Numbers (if present)
   - Address information (street address, city, state, zip code)
   - Phone numbers
   - Email addresses

2. Replace the identified PII data with the following masking patterns:
   - Names: Replace with [NAME]
   - Dates of birth: Replace with [DOB]
   - Insurance ID numbers: Replace with [INSURANCE_ID]
   - Social Security Numbers: Replace with [SSN]
   - Address information: Replace with [ADDRESS]
   - Phone numbers: Replace with [PHONE]
   - Email addresses: Replace with [EMAIL]

3. Ensure that you maintain the overall structure and formatting of the document while masking the PII data.

4. If you encounter any other type of information that you believe could be used to identify an individual, use your 
best judgment to mask it with an appropriate label, such as [OTHER_PII].

Here are some examples of how the masking should look:

Original: "Patient: John Doe, DOB: 05/15/1980, Insurance ID: ABC123456789"
Masked: "Patient: [NAME], DOB: [DOB], Insurance ID: [INSURANCE_ID]"

Original: "Please contact Jane Smith at jsmith@email.com or 555-123-4567"
Masked: "Please contact [NAME] at [EMAIL] or [PHONE]"

After processing the document, provide the masked version of the insurance claim document, preserving its original 
structure and formatting as much as possible. Begin your response with <masked_document> and end it with 
</masked_document>.

Remember to carefully review the entire document to ensure all instances of PII have been properly masked.

"""
