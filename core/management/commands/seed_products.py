from django.core.management.base import BaseCommand
from core.models import Product

class Command(BaseCommand):
    help = "Send 10 sample products for PASKAL INSTRUMENT"

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()

        products = [
            dict(name="Bourdon Pressure Gauge 63mm",sku="PI-BPG-63-160", category="Bourdon",
                 short_desc="General purpose gauge for compressors and pumps.",
                 pressure_range="0-160 psi", dial_size="63mm", case_material="MS", connection='1/4" NPT Bottom', price=149.99),

            dict(name="Bourdon Pressure Gauge 100mm",sku="PI-BPG-100-300",category="Bourdon",
                 short_desc="Clear reading dial for industrial systems.",pressure_range="0-300 psi", dial_size="100mm", case_material="MS",connection='1/2" NPT Bottom', price=179.99),

            dict(name="Glycerin Filled Gauge 63mm", sku="PI-GF-63-300", category="Glycerin Filled",
                 short_desc="Stable Pointer in vibration environments.",
                 pressure_range="0-300 psi", dial_size="63mm", case_material="SS", connection='1/4" NPT Bottom', price=149.99),
            
            dict(name="Glycerin Filled Gauge 100mm", sku="PI-GF-100-600", category="Glycerin Filled",
                 short_desc="Best for pumps with vibration and pulsation.",
                 pressure_range="0-600 psi", dial_size="100mm", case_material="SS", connection='1/2" NPT Bottom',price=139.99),

            dict(name="Stainless Steel Gauge 63mm", sku="PI-SS-63-160", category="Stainless Steel",
                 short_desc="Corrosion-resistant construction.",
                 pressure_range ="0-160 psi", dial_size="63mm", case_material="SS", connection='1/4" NPT Back', price=129.99),

            dict(name="Stainless Steel Gauge 100mm", sku="PI-SS-100-300", category="Stainless Steel",
                 short_desc="Harsh environments and industrial media.",
                 pressure_range="0-300 psi", dial_size="100mm", case_material="SS", connection='1/2" NPT Back', price=134.99),
            
            dict(name="Low Pressure Capsule Gauge 63mm", sku="PI-LP-63-15", category="Low Pressure",
                 short_desc="Accurate low pressure readings.",
                 pressure_range="0-15 psi", dial_size="63mm", case_material="MS", connection='1/4" NPT Bottom', price=124.99),
            
            dict(name="High Pressure Gauge 100mm", sku="PI-HP-100-5000", category="High Pressure",
                 short_desc="Heavy duty gauge for high pressure lines.",
                 pressure_range="0-5000 psi", dial_size="100mm", case_material="SS", connection='1/2" NPT Bottom', price=199.99),
                 
            dict(name="Vaccum Gauge 63mm", sku="PI-VAC-63", category="Vaccum",
                 short_desc="Vaccum measurement for pumps & HVAC.",
                 pressure_range="-30 inHg", dial_size="63mm", case_material="MS", connection='1/4" NPT Bottom', price=139.99),

            dict(name="Compoumd Gauge 63mm", sku="PI-CMP-63", category="Compound",
                 short_desc="Pressure + Vaccum in one detail",
                 pressure_range="-1-15 bar", dial_size="63mm", case_material="SS", connection='1/4" NPT bottom', price=119.99),

                 
        ]

        Product.objects.bulk_create([Product(**p) for p in products])
        self.stdout.write(self.style.SUCCESS("Seeded 10 products successful"))