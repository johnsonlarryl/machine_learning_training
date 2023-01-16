import argparse


def predict_prime_rate(): pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--federal_funds_rates', type=argparse.FileType('r'))
    parser.add_argument('--bank_prime_rate', type=argparse.FileType('r'))
    parser.add_argument('--treasury_real_long_term_rates', type=argparse.FileType('r'))
    parser.add_argument('--federal_funds_rates', type=argparse.FileType('r'))

    args = parser.parse_args()
    federal_funds_rates = args.federal_funds_rates.readlines()
    predict_prime_rate()