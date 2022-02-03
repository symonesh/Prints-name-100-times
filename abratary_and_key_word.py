def build_profile(first, last, **user_info):
        """Build a dictionary containing everything we know about a user."""
        profile = {}
        profile['first_name'] = first
        profile['last_name'] = last
        for key,value in profile.items():
            print(key+"="+value)
        for key, value in user_info.items():
            print(key+"="+value)
            #profile[key] = value
        #return profile
#user_profile = build_profile('albert', 'einstein',location='princeton',field='physics',born_in='germany')
#print(user_profile)
build_profile('albert', 'einstein',location='princeton',field='physics',born_in='germany')

