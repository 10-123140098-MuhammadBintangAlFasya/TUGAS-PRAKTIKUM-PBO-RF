import random

# Kelas abstrak Plant
class Plant:
    def __init__(self, name, water_needs, fertilizer_needs):
        # Inisialisasi nama tanaman, kebutuhan air, dan kebutuhan pupuk
        self.name = name
        self.water_needs = water_needs
        self.fertilizer_needs = fertilizer_needs

    def grow(self):
        pass

    def calculate_needs(self, rainfall, soil_moisture):
        if rainfall > 5:
            self.water_needs -= rainfall // 2
            if self.water_needs < 0:
                self.water_needs = 0

    def show_needs(self, rainfall, soil_moisture):
        print(f"Weather Report: Rainfall = {rainfall} mm, Soil Moisture = {soil_moisture}%")
        print(f"Adjusted Water Needs: {self.water_needs} liters" + (" (reduced due to rain)" if rainfall > 5 else ""))
        print(f"Adjusted Fertilizer Needs: {self.fertilizer_needs} kg\n")

# Kelas turunan RicePlant
class RicePlant(Plant):
    def __init__(self):
        super().__init__("Rice", 20, 4)

    def grow(self):
        print(f"{self.name} is growing in the paddy field")

# Kelas turunan CornPlant
class CornPlant(Plant):
    def __init__(self):
        super().__init__("Corn", 18, 7)

    def grow(self):
        print(f"{self.name} is growing in the farm")

# Fungsi simulasi cuaca
def simulate_weather():
    # Menghasilkan curah hujan dan kelembapan tanah secara acak
    rainfall = random.randint(0, 20)
    soil_moisture = random.randint(0, 100)
    return rainfall, soil_moisture

rice = RicePlant()
corn = CornPlant()

rainfall, soil_moisture = simulate_weather()
rice.grow()
rice.calculate_needs(rainfall, soil_moisture)
rice.show_needs(rainfall, soil_moisture)

rainfall, soil_moisture = simulate_weather()
corn.grow()
corn.calculate_needs(rainfall, soil_moisture)
corn.show_needs(rainfall, soil_moisture)