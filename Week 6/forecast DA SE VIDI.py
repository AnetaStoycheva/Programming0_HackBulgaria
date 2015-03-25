from list_functions import count_item

def forecast(days):

    result = ''
    sunshine = count_item("sunshine", days)
    rain = count_item("rain", days)
    snow = count_item("snow", days)

    if rain > sunshine and rain > snow:
        result = "rain"
    elif sunshine > rain and sunshine > snow:
        result = "sunshine"
    elif snow > rain and snow > sunshine:
        result = "snow"
    elif snow == rain and snow > sunshine:
        result = "sunshine"
    elif snow == sunshine and snow > rain:
        result = "rain"
    elif rain == sunshine and rain > snow:
        result = "snow"
    elif rain == sunshine == snow:
        result = days[-1]
    else:
        pass

    return result


def main():
    print(forecast(["snow", "snow", "rain", "sunshine"]))
    print(forecast(["rain", "rain", "snow", "snow", "sunshine", "sunshine"]))
    print(forecast(["rain", "rain", "sunshine", "sunshine"]))


if __name__ == '__main__':
    main()
