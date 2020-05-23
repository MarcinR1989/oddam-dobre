# ODDAM W DOBRE RĘCE

## CEL PROJEKTU
Celem projektu jest stworzenie miejsca, w którym każdy będzie mógł oddać niepotrzebne rzeczy zaufanym instytucjom.

> SKĄD POMYSŁ NA PROJEKT:
> * Użytkownik ma w domu rzeczy, których chce się pozbyć, ale nie wie jak.
> * Jest wiele dostępnych rozwiązań, ale wiele z nich wymaga dodatkowego wysiłku lub nie ma do nich zaufania. W zweryfikowane miejsca trzeba pojechać, a nie ma na to czasu/ nie ma jak tam pojechać, a kontenery pod domem lub lokalne zbiórki są niezweryfikowane i nie wiadomo czy te rzeczy faktycznie trafią do potrzebujących. 

## WYMAGANIA FUNKCJONALNE
1. Landing page który ma zachęcać do skorzystania z aplikacji
2. Profil administratora
    * logowanie
    * zarządzanie (CRUD*) administratorów
    * zarządzanie (CRUD) zaufanych instytucji
    * przegląd złożonych darów
3. Profil użytkownika
    * rejestracja
    * logowanie (ten sam formularz co dla administratora)
    * walidacja poprawnego podania dwóch identycznych haseł
    * dodawanie darów
    * przeglądanie, złożonych darów
### Dodatkowe funkcjonalności
* zaznaczenie, że dar został przekazany (archiwizacja)
* edycja własnego profilu
    * potwierdzenie/aktywacja konta poprzez wiadomość na email podany przy rejestracji
    * obsługa zapomnianych haseł
    * walidacja obsługi administratorów (np. brak możliwości skasowania ostatniego istniejącego administratora
    * obsługa formularza kontaktowego

## WYMAGANIA NIEFUNKCJONALNE
Do aplikacji zostały wykorzystane:
* Python 3
* Django
* PostgreSQL
