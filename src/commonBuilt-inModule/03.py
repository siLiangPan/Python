#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import base64
encode_a=base64.b64encode(b'binary\x00string')
print(encode_a)
decode_a=base64.b64decode(b'YmluYXJ5AHN0cmluZw==')
print(decode_a)
'''
b'YmluYXJ5AHN0cmluZw=='
b'binary\x00string'
'''

encode_b=base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(encode_b)
encode_b=base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(encode_b)
decode_b=base64.urlsafe_b64decode('abcd--__')
print(decode_b)
'''
b'abcd++//'
b'abcd--__'
b'i\xb7\x1d\xfb\xef\xff'
'''
