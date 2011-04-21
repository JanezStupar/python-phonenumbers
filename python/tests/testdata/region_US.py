"""Auto-generated file, do not edit by hand. US metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_US = PhoneMetadata(id='US', country_code=1, international_prefix='011',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[13-9]\d{9}|2[0-35-9]\d{8}', possible_number_pattern=u'\d{7}(?:\d{3})?', example_number=u'1234567890'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'[13-9]\d{9}|2[0-35-9]\d{8}', possible_number_pattern=u'\d{7}(?:\d{3})?', example_number=u'1234567890'),
    mobile=PhoneNumberDesc(national_number_pattern=u'[13-9]\d{9}|2[0-35-9]\d{8}', possible_number_pattern=u'\d{7}(?:\d{3})?', example_number=u'1234567890'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'8(?:00|66|77|88)\d{7}', possible_number_pattern=u'\d{10}', example_number=u'1234567890'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'900\d{7}', possible_number_pattern=u'\d{10}', example_number=u'1234567890'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'800\d{7}', possible_number_pattern=u'\d{10}', example_number=u'1234567890'),
    national_prefix=u'1',
    preferred_extn_prefix=u' extn. ',
    national_prefix_for_parsing=u'1',
    number_format=[NumberFormat(pattern='(\d{3})(\d{3})(\d{4})', format=u'\\1 \\2 \\3'),
        NumberFormat(pattern='(\d{3})(\d{4})', format=u'\\1 \\2')],
    intl_number_format=[NumberFormat(pattern='(\d{3})(\d{3})(\d{4})', format=u'\\1 \\2 \\3')],
    main_country_for_code=True)
