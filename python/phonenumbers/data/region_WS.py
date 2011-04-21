"""Auto-generated file, do not edit by hand. WS metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_WS = PhoneMetadata(id='WS', country_code=685, international_prefix='0',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[2-8]\d{4,6}', possible_number_pattern=u'\d{5,7}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'(?:[2-5]\d|6[1-9]|840\d)\d{3}', possible_number_pattern=u'\d{5,7}', example_number=u'22123'),
    mobile=PhoneNumberDesc(national_number_pattern=u'(?:60|7[25-7]\d)\d{4}', possible_number_pattern=u'\d{6,7}', example_number=u'601234'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'800\d{3}', possible_number_pattern=u'\d{6}', example_number=u'800123'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    national_prefix=u'0',
    national_prefix_for_parsing=u'0',
    number_format=[NumberFormat(pattern='(8[04]0)(\d{3,4})', format=u'\\1 \\2', leading_digits_pattern=['8[04]0'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(7[25-7])(\d{5})', format=u'\\1 \\2', leading_digits_pattern=['7[25-7]'], national_prefix_formatting_rule=u'0\\1')])
