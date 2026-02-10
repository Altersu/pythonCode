class Phone:
    IMEI = None
    producer = "IPhone"

    def call_by_4g(self):
        print("4G call")

class Phone2022(Phone):
    face_id = "10001"

    def call_by_5g(self):
        print("5G call")

# phone = Phone2022()
# print(phone.producer)
# phone.call_by_5g()
# phone.call_by_4g()

class NFCReader:
    nfc_type = "第五代"
    producer = "HM"

    def read_card(self):
        print("NFC 读卡")

    def write_card(self):
        print("NFC 写卡")

class RemoteControl:
    rc_type = "红外遥控"
    def control(self):
        print("红外遥控开启了")

class MyPhone(Phone2022, NFCReader, RemoteControl) :
    pass

phone = MyPhone()
phone.call_by_5g()
phone.read_card()
phone.control()
print(phone.nfc_type)
print(phone.producer)
