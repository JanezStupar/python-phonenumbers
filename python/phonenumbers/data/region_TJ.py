"""Auto-generated file, do not edit by hand. TJ metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_TJ = PhoneMetadata(id='TJ', country_code=992, international_prefix='8~10',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[349]\d{8}', possible_number_pattern=u'\d{3,9}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'(?:3(?:1[3-5]|2[245]|31|4[24-7]|5[25]|72)|4(?:46|74|87))\d{6}', possible_number_pattern=u'\d{3,9}', example_number=u'372123456'),
    mobile=PhoneNumberDesc(national_number_pattern=u'9[0-35-9]\d{7}', possible_number_pattern=u'\d{9}', example_number=u'917123456'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    national_prefix=u'8',
    national_prefix_for_parsing=u'8',
    number_format=[NumberFormat(pattern='([349]\d{2})(\d{2})(\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['[34]7|91[78]'], national_prefix_formatting_rule=u'8\\1'),
        NumberFormat(pattern='([49]\d)(\d{3})(\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['4[48]|9(?:19|[0235-9])'], national_prefix_formatting_rule=u'8\\1'),
        NumberFormat(pattern='(331700)(\d)(\d{2})', format=u'\\1 \\2 \\3', leading_digits_pattern=['331', '3317', '33170', '331700'], national_prefix_formatting_rule=u'8\\1'),
        NumberFormat(pattern='(\d{4})(\d)(\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['3[1-5]', '3(?:[1245]|3(?:[02-9]|1[0-589]))'], national_prefix_formatting_rule=u'8\\1')])
