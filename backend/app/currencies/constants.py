STATUS_ACTIVE = 'ACTIVE'
STATUS_DRAFT = 'DRAFT'
STATUS_DELETED = 'DELETED'  # For soft delete purposes

CURRENCY_STATUS = (
    (STATUS_ACTIVE, 'Active'),  # Currencies available for operate
    (STATUS_DRAFT, 'Draft'),
    (STATUS_DELETED, 'Deleted'),
    # Add more statuses like COMING_SOON
)
