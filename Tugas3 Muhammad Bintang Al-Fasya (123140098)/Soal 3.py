class BankAccount:
    # Kurs konversi tetap antara mata uang
    exchange_rates = {
        ('USD', 'EUR'): 0.9,
        ('EUR', 'USD'): 1.1,
        ('USD', 'IDR'): 16500,
        ('IDR', 'USD'): 1/16500,
        ('EUR', 'IDR'): 17500,
        ('IDR', 'EUR'): 1/17500
    }

    def __init__(self, account_holder, balance, currency):
        self.account_holder = account_holder
        self.balance = balance
        self.currency = currency

    # Metode untuk menampilkan informasi akun
    def __str__(self):
        return f"{self.account_holder}'s Account: Balance = {self.currency} {self.balance:.2f}"

    # Menambahkan bunga berdasarkan saldo
    def apply_interest(self):
        if self.balance > 5000:
            persen_bunga = 0.02
        else:
            persen_bunga = 0.01
        bunga = self.balance * persen_bunga
        self.balance += bunga
        print(f"Applying interest... New Balance = {self.currency} {self.balance:.2f}")

    # Melakukan konversi mata uang
    def convert_currency(self, target_currency):
        if self.currency == target_currency:
            return self.balance
        rate = self.exchange_rates.get((self.currency, target_currency), None)
        return self.balance * rate

    # Operator tambah untuk transaksi lintas mata uang
    def __add__(self, other):
        converted_balance = other.convert_currency(self.currency)
        new_balance = self.balance + converted_balance
        return BankAccount(self.account_holder, new_balance, self.currency)

    # Operator kurang untuk transaksi lintas mata uang
    def __sub__(self, other):
        converted_balance = other.convert_currency(self.currency)
        if self.balance < converted_balance:
            print("Insufficient balance for withdrawal!")
            print(f"{self.account_holder}'s Account: Balance remains at {self.currency} {self.balance:.2f}")
            return self
        new_balance = self.balance - converted_balance
        return BankAccount(self.account_holder, max(new_balance, 0), self.currency)

Tono = BankAccount("Tono", 5000, "USD")
print(Tono)
Tono.apply_interest()
print(Tono)

Budi = BankAccount("Budi", 1000, "EUR")
print(Budi)
converted = Budi.convert_currency("USD")
print(f"Converted to USD: ${converted:.2f}")

withdrawal = BankAccount("", 1200, "USD")
Budi = Budi - withdrawal
print(Budi)
