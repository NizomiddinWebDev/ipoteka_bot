from aiogram.dispatcher.filters.state import State, StatesGroup

class UserState(StatesGroup):
    start = State()
    language = State()
    contact = State()
    verification = State()
    main_menu = State()
    personal = State()
    child = State()
    personal_deposit_source = State()
    personal_deposit_currency = State()
    personal_deposit_bank = State()
    personal_deposit_mobile = State()
    personal_credit_type = State()
    personal_credit = State()
    personal_card_currency = State()
    personal_card = State()
    personal_national_card = State()
    personal_internation_card = State()
    # into personal vkladi
    contributions = State()
    contributions_via_bank = State()
    contributions_via_mobile = State()
    contributions_national_pay = State()
    # 3 value
    contributions_internation_pay = State()
    corporate = State()
    entrepreneur = State()
    regions = State()
    branches = State()
    branches_tashkent = State()
    settings = State()
    change_language = State()
    contact_us = State()
    write_consultant = State()
    # 1 value only

    money_transfers = State()
    money_transfers_western = State()
    money_transfers_golden_crone = State()
    money_transfers_western_oae = State()
    money_transfers_western_central_asia = State()
    money_transfers_western_central_china = State()
    money_transfers_western_all = State()

    money_transfers_unistream = State()
    money_transfers_ria = State()
    money_transfers_moneygram = State()
    money_transfers_contact = State()
    money_transfers_asia_express = State()
    # contributions_via_mobile = 65
    # consumer credit
    personal_credit_consumer_type = State()
    personal_consumer_credit = State()
    # send message only values 2