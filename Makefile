SIM ?= icarus
TOPLEVEL_LANG ?= verilog

VERILOG_SOURCES += $(PWD)/and_gate.v
TOPLEVEL = and_gate
MODULE = test_and

include $(shell cocotb-config --makefiles)/Makefile.sim
