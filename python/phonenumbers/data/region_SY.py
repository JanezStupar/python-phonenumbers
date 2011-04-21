"""Auto-generated file, do not edit by hand. SY metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_SY = PhoneMetadata(id='SY', country_code=963, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[1-59]\d{7,8}', possible_number_pattern=u'\d{6,9}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'(?:1(?:1\d?|4\d|[2356])|2[1-35]|3(?:1\d|[34])|4[13]|5[1-3])\d{6}', possible_number_pattern=u'\d{6,9}', example_number=u'112345678'),
    mobile=PhoneNumberDesc(national_number_pattern=u'9(?:3[23]|4[457]|55|6[67]|88|9[19])\d{6}', possible_number_pattern=u'\d{9}', example_number=u'944567890'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    national_prefix=u'0',
    national_prefix_for_parsing=u'0',
    number_format=[NumberFormat(pattern='(\d{2})(\d{3})(\d{3,4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['[1-5]'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(9[3-689])(\d{4})(\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['9'], national_prefix_formatting_rule=u'0\\1')])
