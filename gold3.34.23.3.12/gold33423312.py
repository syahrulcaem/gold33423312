class KonversiJarak:
    @staticmethod
    def km_ke_mil(km):
        return km * 0.621371

    @staticmethod
    def mil_ke_km(mil):
        return mil * 1.60934

    @staticmethod
    def km_ke_meter(km):
        return km * 1000

    @staticmethod
    def meter_ke_km(meter):
        return meter / 1000
    
    def hitung_golden_ratio():
        golden_ratio = (1 + 5 ** 0.5) / 2
        return golden_ratio
