
def separate_channels(image):
    separated_channels_list = []
    for k in range(len(image[0][0])):
        for i in range(len(image)):
            for j in range(len(image[0])):
                if len(separated_channels_list) <= k:
                    separated_channels_list.append([])
                if len(separated_channels_list[k]) <= i:
                    separated_channels_list[k].append([])
                separated_channels_list[k][i].append(image[i][j][k])
    return separated_channels_list


def combine_channels(channels):
    return separate_channels(separate_channels(channels))


def RGB2grayscale(colored_image):
    gray_scale_image = []
    for i in range(len(colored_image)):
        for j in range(len(colored_image[0])):
            if len(gray_scale_image) <= i:
                gray_scale_image.append([])
            if len(gray_scale_image[i]) <= j:
                gray_scale_image[i].append([])
            gray_scale_image[i][j] = round(colored_image[i][j][0] * 0.299) + round(
                colored_image[i][j][1] * 0.587) + round(colored_image[i][j][2] * 0.114)
    return gray_scale_image


