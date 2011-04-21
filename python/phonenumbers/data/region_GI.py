"""Auto-generated file, do not edit by hand. GI metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_GI = PhoneMetadata(id='GI', country_code=350, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[2568]\d{7}', possible_number_pattern=u'\d{8}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'2(?:00\d|16[0-7]|22[2457])\d{4}', possible_number_pattern=u'\d{8}', example_number=u'20012345'),
    mobile=PhoneNumberDesc(national_number_pattern=u'(?:5[4-8]|60)\d{6}', possible_number_pattern=u'\d{8}', example_number=u'57123456'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'80\d{6}', possible_number_pattern=u'\d{8}', example_number=u'80123456'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'8[1-689]\d{6}', possible_number_pattern=u'\d{8}', example_number=u'88123456'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'87\d{6}', possible_number_pattern=u'\d{8}', example_number=u'87123456'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'))
