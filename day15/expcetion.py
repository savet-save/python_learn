#异常
try:
    1 / 0
except:
    print("error")

try:
    1 / 0
except ZeroDivisionError:
    print("error")

try:
    1 / 0
except ZeroDivisionError as e:
    print("error : ", e)

try:
    1 / 0
except (ZeroDivisionError, TypeError) as e:
    print("error : ", e)

try:
    1 / 0
except ZeroDivisionError as e:
    print("error : ", e)
except TypeError:
    print("error")

try:
    1 / 1
except ZeroDivisionError as e:
    print("error : ", e)
else:
    print("ok")

try:
    1 / 0
except ZeroDivisionError as e:
    print("error : ", e)
finally:
    print("end")

try:
    1 + 1
    try:
        1 + "1"
    except:
        print("error1")
except:
    print("error2")

#raise
try:
    raise ValueError("error3")
except ValueError as e:
    print("error : ", e)

#异常链
try:
    raise ValueError("error4") from ZeroDivisionError
except ValueError as e:
    print("error : ", e)

#assert
try:
    assert 1 == 2
except AssertionError:
    print("error")

