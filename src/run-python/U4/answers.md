### Ex : a friendly converter with user input
---

```python
c = input("Please choose a temperature to convert : ")


def temp_conv(c):
    result = (float(c) * 9 / 5) + 32
    message = (
        str(c)
        + " "
        + "degrees Celsius are"
        + " "
        + str(result)
        + " "
        + "degrees Farenheit !"
    )
    return message


friendly_temp = temp_conv(c)
print(friendly_temp)
```
---
