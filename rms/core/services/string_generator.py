from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from typing import List

import random


class RandomString:

    _groups_dict = {
        'digits': digits,
        'punctuation': punctuation,
        'lowercase': ascii_lowercase,
        'uppercase': ascii_uppercase,
    }


    @staticmethod
    def _symbols_set_formation(
        include_groups: List[str],
        include_explicit: str = '',
        exclude_explicit: str = '',
    ) -> str:
        """
        Forms a set of symbols based on the specified groups, explicit inclusions, and exclusions.

        Args:
            include_groups (List[str]): List of symbol groups to include in the set.
            include_explicit (str, optional): Explicit symbols to include in the set. Defaults to ''.
            exclude_explicit (str, optional): Explicit symbols to exclude from the set. Defaults to ''.

        Returns:
            str: The resulting string of symbols.
        
        Raises:
            ValueError: If an invalid symbol group or blank symbol is included.

        """

        result = set()

        for group in include_groups:
            group_ = group.lower().strip()

            if group_ not in RandomString._groups_dict.keys():
                raise ValueError(f"Unable to include '{group if group.strip() else 'empty'}' symbols group")

            result.update(set(RandomString._groups_dict[group_]))
        
        include_explicit = include_explicit.strip()
        exclude_explicit = exclude_explicit.strip()

        if include_explicit:
            if ' ' in include_explicit:
                raise ValueError("Unable to include blank symbol")
            result.update(set(include_explicit))
        
        if exclude_explicit:
            result.difference_update(set(exclude_explicit))
        
        return "".join(result)


    @classmethod
    def get_random_string(
        self,
        length: int,
        **kwargs,
    ) -> str:
        """
        Generates a random string of specified length.

        Args:
            length (int): The length of the random string.
            **kwargs: Additional keyword arguments for symbol configuration.

        Returns:
            str: The generated random string.

        """

        symbols_sheet = self._symbols_set_formation(**kwargs)
        random_string = "".join([random.choice(symbols_sheet) for _ in range(length)])

        return random_string


    @classmethod
    def get_random_username(
        self,
        length: int = 15,
        include_groups: List[str] = ['lowercase', 'digits',],
        **kwargs,
    ) -> str:
        """
        Generates a random username with the specified length and symbol configurations.

        Args:
            length (int, optional): The length of the username. Defaults to 15.
            include_groups (List[str], optional): List of symbol groups to include in the username. Defaults to ['lowercase', 'digits'].
            **kwargs: Additional keyword arguments for symbol configuration.

        Returns:
            str: The generated random username.

        """

        return self.get_random_string(length=length, include_groups=include_groups, **kwargs)


    @classmethod
    def get_random_token(
        self,
        length: int = 64,
        include_groups: List[str] = ['lowercase', 'digits', 'uppercase',],
        **kwargs,
    ) -> str:
        """
        Generates a random token with the specified length and symbol configurations.

        Args:
            length (int, optional): The length of the token. Defaults to 64.
            include_groups (List[str], optional): List of symbol groups to include in the token. Defaults to ['lowercase', 'digits', 'uppercase'].
            **kwargs: Additional keyword arguments for symbol configuration.

        Returns:
            str: The generated random token.

        """

        return self.get_random_string(length=length, include_groups=include_groups, include_explicit='-', **kwargs)
