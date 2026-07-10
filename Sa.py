import subprocess

def run_adb_command():
    print("--- ADB ချိတ်ဆက်မှု စစ်ဆေးခြင်း ---")
    try:
        # adb devices command ကို ဖုန်းထဲမှာ Run ကြည့်ခြင်း
        result = subprocess.check_output(["adb", "devices"]).decode("utf-8")
        print("ရလဒ်:")
        print(result)
    except Exception as e:
        print("အမှားဖြစ်ပွားသည်: ADB မတွေ့ရှိပါ (သို့) USB Debugging မဖွင့်ရသေးပါ။")

if __name__ == "__main__":
    run_adb_command()
