"""Auto-generated file, do not edit by hand. MV metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_MV = PhoneMetadata(id='MV', country_code=960, international_prefix='0(?:0|19)',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[367]\d{6}|9(?:00\d{7}|\d{6})', possible_number_pattern=u'\d{7,10}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'(?:3(?:0[01]|3[0-59]|)|6(?:[567][02468]|8[024689]|90))\d{4}', possible_number_pattern=u'\d{7}', example_number=u'6701234'),
    mobile=PhoneNumberDesc(national_number_pattern=u'(?:7[36-9]|9[6-9])\d{5}', possible_number_pattern=u'\d{7}', example_number=u'7712345'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'900\d{7}', possible_number_pattern=u'\d{10}', example_number=u'9001234567'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'781\d{4}', possible_number_pattern=u'\d{7}', example_number=u'7812345'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    preferred_international_prefix=u'00',
    number_format=[NumberFormat(pattern='(\d{3})(\d{4})', format=u'\\1-\\2', leading_digits_pattern=['[367]|9(?:[1-9]|0[1-9])']),
        NumberFormat(pattern='(\d{3})(\d{3})(\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['900'])])
