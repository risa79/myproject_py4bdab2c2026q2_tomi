from myproject_py4bdab2c2026q2_tomi.main import is_prime, primes, checksum, pipeline

def test_is_prime():
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False
    assert is_prime(11) is True
    assert is_prime(1) is False

def test_primes_count():
    assert len(primes(10)) == 10

def test_checksum_small():
    data = [2, 3, 5]
    assert checksum(data) == 2924666

def test_pipeline_target_result():
    assert pipeline(1000, 100) == 7785816
