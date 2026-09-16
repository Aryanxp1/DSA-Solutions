class Solution:
  def toHex(self, num: int) -> str:
    # If the input number is zero, return '0'
    if num == 0:
        return '0'
    # If the input number is negative, convert it to its corresponding positive value using two's complement
    if num < 0:
        num = (1 << 32) + num
    
    hex_digits = '0123456789abcdef'  # The hexadecimal digits
    
    hex_num = ''  # Initialize an empty string to store the hexadecimal representation of the input number
    
    # Repeatedly divide the input number by 16 and convert the remainder to its corresponding hexadecimal digit until the quotient becomes zero
    while num > 0:
        digit = num % 16  # Get the remainder of dividing the input number by 16
        hex_digit = hex_digits[digit]  # Convert the remainder to its corresponding hexadecimal digit
        hex_num = hex_digit + hex_num  # Add the hexadecimal digit to the beginning of the hexadecimal representation
        num //= 16  # Update the input number by dividing it by 16
    
    return hex_num
