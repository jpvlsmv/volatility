# Volatility
# Copyright (c) 2008-2013 Volatility Foundation
#
# This file is part of Volatility.
#
# Volatility is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License Version 2 as
# published by the Free Software Foundation.  You may not use, modify or
# distribute this program under any other version of the GNU General
# Public License.
#
# Volatility is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Volatility.  If not, see <http://www.gnu.org/licenses/>.
#

crash_vtypes = {
## These types are for crash dumps
  '_DMP_HEADER' : [ 0x1000, {
    'Signature' : [ 0x0, ['array', 4, ['unsigned char']]],
    'ValidDump' : [ 0x4, ['array', 4, ['unsigned char']]],
    'MajorVersion' : [ 0x8, ['unsigned int']],
    'MinorVersion' : [ 0xc, ['unsigned int']],
    'DirectoryTableBase' : [ 0x10, ['unsigned int']],
    'PfnDataBase' : [ 0x14, ['unsigned int']],
    'PsLoadedModuleList' : [ 0x18, ['unsigned int']],
    'PsActiveProcessHead' : [ 0x1c, ['unsigned int']],
    'MachineImageType' : [ 0x20, ['unsigned int']],
    'NumberProcessors' : [ 0x24, ['unsigned int']],
    'BugCheckCode' : [ 0x28, ['unsigned int']],
    'BugCheckCodeParameter' : [ 0x2c, ['array', 4, ['unsigned int']]],
    'VersionUser' : [ 0x3c, ['array', 32, ['unsigned char']]],
    'PaeEnabled' : [ 0x5c, ['unsigned char']],
    'KdSecondaryVersion' : [ 0x5d, ['unsigned char']],
    'VersionUser2' : [ 0x5e, ['array', 2, ['unsigned char']]],
    'KdDebuggerDataBlock' : [ 0x60, ['unsigned int']],
    'PhysicalMemoryBlockBuffer' : [ 0x64, ['_PHYSICAL_MEMORY_DESCRIPTOR']],
    'ContextRecord' : [ 0x320, ['array', 1200, ['unsigned char']]],
    'Exception' : [ 0x7d0, ['_EXCEPTION_RECORD32']],
    'Comment' : [ 0x820, ['array', 128, ['unsigned char']]],
    'DumpType' : [ 0xf88, ['unsigned int']],
    'MiniDumpFields' : [ 0xf8c, ['unsigned int']],
    'SecondaryDataState' : [ 0xf90, ['unsigned int']],
    'ProductType' : [ 0xf94, ['unsigned int']],
    'SuiteMask' : [ 0xf98, ['unsigned int']],
    'WriterStatus' : [ 0xf9c, ['unsigned int']],
    'RequiredDumpSpace' : [ 0xfa0, ['unsigned int']],
    'SystemUpTime' : [ 0xfb8, ['unsigned int']],
    'SystemTime' : [ 0xfc0, ['unsigned int']],
    'reserved3' : [ 0xfc8, ['array', 56, ['unsigned char']]],
} ],
  '_DMP_HEADER64' : [ 0x2000, {
    'Signature' : [ 0x0, ['array', 4, ['unsigned char']]],
    'ValidDump' : [ 0x4, ['array', 4, ['unsigned char']]],
    'MajorVersion' : [ 0x8, ['unsigned int']],
    'MinorVersion' : [ 0xc, ['unsigned int']],
    'DirectoryTableBase' : [ 0x10, ['unsigned int']],
    'PfnDataBase' : [ 0x18, ['unsigned int']],
    'PsLoadedModuleList' : [ 0x20, ['unsigned int']],
    'PsActiveProcessHead' : [ 0x28, ['unsigned int']],
    'MachineImageType' : [ 0x30, ['unsigned int']],
    'NumberProcessors' : [ 0x34, ['unsigned int']],
    'BugCheckCode' : [ 0x38, ['unsigned int']],
    'BugCheckCodeParameter' : [ 0x40, ['array', 4, ['unsigned int']]],
    'KdDebuggerDataBlock' : [0x80, ['unsigned int']],
    'PhysicalMemoryBlockBuffer' : [ 0x88, ['_PHYSICAL_MEMORY_DESCRIPTOR']],
    'ContextRecord' : [ 0x348, ['array', 3000, ['unsigned char']]],
    'Exception' : [ 0xf00, ['_EXCEPTION_RECORD64']],
    'DumpType' : [ 0xf98, ['unsigned int']],
    'RequiredDumpSpace' : [ 0xfa0, ['unsigned int']],
    'SystemTime' : [ 0xfa8, ['unsigned int']],
    'Comment' : [ 0xfb0, ['array', 128, ['unsigned char']]],
    'SystemUpTime' : [ 0x1030, ['unsigned int']],
    'MiniDumpFields' : [ 0x1038, ['unsigned int']],
    'SecondaryDataState' : [ 0x103c, ['unsigned int']],
    'ProductType' : [ 0x1040, ['unsigned int']],
    'SuiteMask' : [ 0x1044, ['unsigned int']],
    'WriterStatus' : [ 0x1048, ['unsigned int']],
    'Unused1' : [ 0x104c, ['unsigned char']],
    'KdSecondaryVersion' : [ 0x104d, ['unsigned char']],
    'Unused' : [ 0x104e, ['array', 2, ['unsigned char']]],
    '_reserved0' : [ 0x1050, ['array', 4016, ['unsigned char']]],
} ],
}
