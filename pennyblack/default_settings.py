from django.conf import settings

TINYMCE_CONFIG_URL = getattr(settings, 'PENNYBLACK_TINYMCE_CONFIG_URL', 'admin/content/richtext/init.html')

LANGUAGES = getattr(settings, 'LANGUAGES')

JOB_STATUS = getattr(settings, 'PENNYBLACK_JOB_STATUS', ((1,'Draft'),(11,'Pending'),(21,'Sending'),(31,'Finished'),(41,'Error'),(42,'Timeout (will retry)')))

JOB_STATUS_CAN_SEND = getattr(settings, 'PENNYBLACK_JOB_STATUS_CAN_SEND', (1,41))
JOB_STATUS_PENDING = getattr(settings, 'PENNYBLACK_JOB_STATUS_PENDING', (11,42))
JOB_STATUS_CAN_EDIT = getattr(settings, 'PENNYBLACK_JOB_STATUS_CAN_EDIT', (1,))

# bounce detection
BOUNCE_DETECTION_ENABLE = getattr(settings, 'PENNYBLACK_BOUNCE_DETECTION_ENABLE', True)
BOUNCE_DETECTION_DAYS_TO_LOOK_BACK = getattr(settings, 'PENNYBLACK_BOUNCE_DETECTION_DAYS_TO_LOOK_BACK',5)

# content
NEWSLETTER_CONTENT_WIDTH = getattr(settings, 'PENNYBLACK_NEWSLETTER_WIDTH', 600)

TEXT_AND_IMAGE_CONTENT_POSITIONS = getattr(settings, 'PENNYBLACK_TEXT_AND_IMAGE_CONTENT_POSITIONS', (('left','Left'),('right','Right'),('top','Top')))
TEXT_AND_IMAGE_CONTENT_IMAGE_WIDTH_SIDE = getattr(settings, 'PENNYBLACK_TEXT_AND_IMAGE_CONTENT_IMAGE_WIDTH_SIDE', 100)