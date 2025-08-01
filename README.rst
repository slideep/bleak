=====
Bleak
=====

.. image:: https://github.com/hbldh/bleak/workflows/Build%20and%20Test/badge.svg
    :target: https://github.com/hbldh/bleak/actions?query=workflow%3A%22Build+and+Test%22
    :alt: Build and Test

.. image:: https://img.shields.io/pypi/v/bleak.svg
    :target: https://pypi.python.org/pypi/bleak

.. image:: https://img.shields.io/pypi/dm/bleak.svg
    :target: https://pypi.python.org/pypi/bleak
    :alt: PyPI - Downloads

.. image:: https://readthedocs.org/projects/bleak/badge/?version=latest
    :target: https://bleak.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black

.. container::

    .. image:: Bleak_logo2.png
        :target: https://github.com/hbldh/bleak
        :alt: Bleak Logo

Bleak is an acronym for Bluetooth Low Energy platform Agnostic Klient.

* Free software: MIT license
* Documentation: https://bleak.readthedocs.io.

Bleak is a GATT client software, capable of connecting to BLE devices
acting as GATT servers. It is designed to provide a asynchronous,
cross-platform Python API to connect and communicate with e.g. sensors.

Installation
------------

.. code-block:: bash

    $ pip install bleak

Features
--------

* Supports Windows 10, version 16299 (Fall Creators Update) or greater
* Supports Linux distributions with BlueZ >= 5.55
* OS X/macOS support via Core Bluetooth API, from at least OS X version 10.13
* Android backend compatible with python-for-android

Bleak supports reading, writing and getting notifications from
GATT servers, as well as a function for discovering BLE devices.

Usage
-----

To discover Bluetooth devices that can be connected to:

.. code-block:: python

    import asyncio
    from bleak import BleakScanner

    async def main():
        devices = await BleakScanner.discover()
        for d in devices:
            print(d)

    asyncio.run(main())


Connect to a Bluetooth device and read its model number:

.. code-block:: python

    import asyncio
    from bleak import BleakClient

    address = "24:71:89:cc:09:05"
    MODEL_NBR_UUID = "2A24"

    async def main(address):
        async with BleakClient(address) as client:
            model_number = await client.read_gatt_char(MODEL_NBR_UUID)
            print("Model Number: {0}".format("".join(map(chr, model_number))))

    asyncio.run(main(address))

DO NOT NAME YOUR SCRIPT ``bleak.py``! It will cause a circular import error.

See examples folder for more code, for instance example code for connecting to a
`TI SensorTag CC2650 <http://www.ti.com/ww/en/wireless_connectivity/sensortag/>`_
