import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_and_gate(dut):
    """用 Python 自動測試 AND 閘的所有輸入組合"""
    
    # 列出所有要測試的 (a, b) 組合
    test_cases = [(0, 0), (0, 1), (1, 0), (1, 1)]

    for a_val, b_val in test_cases:
        # 1. 從 Python 把訊號灌進 Verilog 的接腳
        dut.a.value = a_val
        dut.b.value = b_val

        # 2. 等待 10 ns 讓組合邏輯穩定
        await Timer(10, units="ns")

        # 3. 讀取 Verilog 算出的結果，並用 Python assert 自動比對
        actual_y = int(dut.y.value)
        expected_y = a_val & b_val
        
        dut._log.info(f"輸入 a={a_val}, b={b_val} -> 輸出 y={actual_y} (預期={expected_y})")
        assert actual_y == expected_y, f"錯誤！當 a={a_val}, b={b_val} 時，y 應該是 {expected_y}，但得到 {actual_y}"
