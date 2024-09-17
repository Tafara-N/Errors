"""
If we get an error about positional arguments:

TypeError: Generator.add_provider() takes 2 positional arguments but 3 were given
=================================================================================

Traceback (most recent call last):
  File "/home/tafara/Documents/Code/Python/core/faker/./adding_providers.py", line 91, in <module>
    fake.add_provider(CustomProvider, SABanksProvider)
TypeError: Generator.add_provider() takes 2 positional arguments but 3 were given

----------------------

This means the add_provider() method only takes one argument, if we want to add more custom providers, we have to add them one by one.

Example:
=======
# Add the custom provider to the faker instance
fake.add_provider(CustomProvider)
fake.add_provider(SABanksProvider)

"""
