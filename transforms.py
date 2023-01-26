from torchvision.transforms import (
    RandomResizedCrop,
    RandomHorizontalFlip,
    RandomVerticalFlip,
    ColorJitter,
    RandomGrayscale,
    RandomApply,
    Compose,
    GaussianBlur,
    Resize,
    ToTensor,
    RandomRotation,
    RandomAffine,
    Normalize
)

def get_complete_transform(output_shape, kernel_size, s=1.0):
    """
    The color distortion transform.
    
    Args:
        s: Strength parameter.
    
    Returns:
        A color distortion transform.
    """
    rnd_crop = Resize(output_shape)    # random crop
    rnd_flip = RandomHorizontalFlip(p=0.5)     # random flip
    rnd_vflip= RandomVerticalFlip(p=0.5)
    rnd_rotate = RandomRotation(degrees=(-90, 90), fill=(0,))
#     color_jitter = ColorJitter(0.01*s, 0.02*s, 0.08*s, 0.1*s)
#     rnd_color_jitter = RandomApply([color_jitter], p=0.8)      # random color jitter
    rnd_aff= RandomAffine(degrees=(-180, 180), translate=(0.2, 0.2))
#     rnd_gray = RandomGrayscale(p=0.2)    # random grayscale
    gblur =GaussianBlur(kernel_size=9, sigma=(0.1, 0.5))
#     norm= Normalize((0.125753653049469, 0.02737451672554016, 0.02293757855892181), (0.02670302987098694, 0.02240527391433716, 0.0286241775751114))
    to_tensor = ToTensor()
    image_transform = Compose([
        to_tensor,
        rnd_crop,
        rnd_flip,
        rnd_rotate,
#         rnd_gray,
        rnd_vflip,
        rnd_aff,
        gblur
#         norm
    ])
    return image_transform


# generate two views for an image
class ContrastiveLearningViewGenerator(object):
    """Take two random crops of one image as the query and key."""

    def __init__(self, base_transform, n_views=2):
        self.base_transform = base_transform
        self.n_views = n_views

    def __call__(self, x):
        views = [self.base_transform(x) for i in range(self.n_views)]
        return views