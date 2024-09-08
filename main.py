from codecarbon import track_emissions


@track_emissions()
def my_function_to_track():
    for each in range(100):
        print(each)


if __name__ == "__main__":
    my_function_to_track()
