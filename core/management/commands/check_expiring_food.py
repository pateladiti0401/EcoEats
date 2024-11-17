# core/management/commands/check_expiring_food.py
from django.core.management.base import BaseCommand
from django.utils.timezone import now
from datetime import timedelta
from core.models import FoodItem
from core.utils import send_email_notification

class Command(BaseCommand):
    help = "Send email notifications for expiring food items"

    def handle(self, *args, **kwargs):
        today = now().date()
        soon_expiring_foods = FoodItem.objects.filter(
            expiration_date__in=[today + timedelta(days=1), today + timedelta(days=2)]
        )

        for food_item in soon_expiring_foods:
            subject = f"Food Expiry Alert: {food_item.name}"
            message = (
                f"Hello {food_item.user.username},\n\n"
                f"Your food item '{food_item.name}' is expiring soon! "
                f"It will expire on {food_item.expiration_date}.\n\n"
                "Please use it soon or consider donating it to avoid waste.\n\n"
                "Regards,\nEcoEats Team"
            )
            recipient_list = [food_item.user.email]
            send_email_notification(subject, message, recipient_list)

            self.stdout.write(
                f"Notification sent to {food_item.user.email} for {food_item.name}"
            )
